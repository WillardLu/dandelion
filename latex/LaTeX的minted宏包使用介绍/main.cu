#include <math.h>
#include <stdio.h>

const double EPSILON = 1.0e-15;
const double a = 1.23;
const double b = 2.34;
const double c = 3.57;
void __global__ add(const double *x, const double *y, double *z);
void check(const double *z, const int N);

int main(void) {
  // 原书中的N值为1亿（作者所用显卡的显存有8G），已经超过我现用显卡的显存（2G）；
  // 再加上其他方面对显存的消耗，所以这里将N值设为7千万。
  const int N = 50000000;
  const int M = sizeof(double) * N;
  // 下面是在主机中分配内存
  double *h_x = (double*)malloc(M);
  if (h_x == NULL) {
    printf("h_x: Failed to allocate host memory!\n");
    return 1;
  }
  double *h_y = (double*)malloc(M);
  if (h_y == NULL) {
    printf("h_y: Failed to allocate host memory!\n");
    free(h_x);
    return 1;
  }
  double *h_z = (double*)malloc(M);
  if (h_z == NULL) {
    printf("h_z: Failed to allocate host memory!\n");
    free(h_x);
    free(h_z);
    return 1;
  }
  
  // 数组元素初始化
  for (int n = 0; n < N; ++n) {
    h_x[n] = a;
    h_y[n] = b;
  }
  
  double *d_x, *d_y, *d_z;
  // 在显卡中分配显存
  cudaError err;// 判断显存分配是否成功
  err = cudaMalloc((void **)&d_x, M);
  if (err != cudaSuccess) {
    printf("d_x: cudaMemcpy Error!\n");
    free(h_x);
    free(h_y);
    free(h_z);
    return 1;
  }
  err = cudaMalloc((void **)&d_y, M);
  if (err != cudaSuccess) {
    printf("d_y: cudaMemcpy Error!\n");
    free(h_x);
    free(h_y);
    free(h_z);
    cudaFree(d_x);
    return 1;
  }
  err = cudaMalloc((void **)&d_z, M);
  if (err != cudaSuccess) {
    printf("d_z: cudaMemcpy Error!\n");
    free(h_x);
    free(h_y);
    free(h_z);
    cudaFree(d_x);
    cudaFree(d_y);
    return 1;
  }
  // 把主机中的数据复制到显存中
  cudaMemcpy(d_x, h_x, M, cudaMemcpyHostToDevice);
  cudaMemcpy(d_y, h_y, M, cudaMemcpyHostToDevice);
  
  // 设置线程块大小为128，网格大小为N/128=546875。
  const int block_size = 128;
  const int grid_size = N / block_size;
  add<<<grid_size, block_size>>>(d_x, d_y, d_z);
  
  // 把计算结果从显存复制到主机
  cudaMemcpy(h_z, d_z, M, cudaMemcpyDeviceToHost);
  // 检查结果
  check(h_z, N);
  
  // 释放内存、显存
  free(h_x);
  free(h_y);
  free(h_z);
  cudaFree(d_x);
  cudaFree(d_y);
  cudaFree(d_z);
  return 0;
}

// 相加
void __global__ add(const double *x, const double *y, double *z) {
  // blockDim.x 的数值等于执行配置中变量 block_size 的数值，在本例中为 128；
  // blockIdx.x 指定一个线程在一个网格中的线程块指标，其取值范围从0到 gridDim.x-1。本例中，即为0到546874；
  // threadIdx.x 指定一个线程在一个线程块中的线程指标，其取值范围从0到 blockDim.x-1。本例中，即为0到127。
  // 显存中的数组与网格、线程块对应，通过下面计算索引值，让每个线程对应的数组进行计算，实现高效的并行计算。
  const int n = blockDim.x * blockIdx.x + threadIdx.x;
  z[n] = x[n] + y[n];
}

// 判断两个浮点数是否相等。注意，不能使用运算符==，而要将两个数的差的绝对值与一个很小的数进行比较。
// 本例中，假定当两个双精度浮点数的差的绝对值小于1e-15（EPISILON）时它们就是相等的。
void check(const double *z, const int N) {
  bool has_error = false;
  for (int n = 0; n < N; ++n) {
    if (fabs(z[n] - c) > EPSILON) {
      has_error = true;
      printf("z[%d] is: %f, c is: %f\n", n, z[n], c);
    }
  }
  printf("%s\n", has_error ? "Has errors": "No errors");
}
