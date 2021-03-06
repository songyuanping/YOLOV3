# 在mybranch上的工作开发完成了！ 
import 	torch
import  time
import multiprocessing

print(multiprocessing.cpu_count())

print(torch.__version__)
print(torch.cuda.is_available(),torch.cuda.device_count())


a = torch.randn(10000, 1000)
b = torch.randn(1000, 2000)

t0 = time.time()
c = torch.matmul(a, b)
t1 = time.time()
print(a.device, t1 - t0, c.norm(2))

