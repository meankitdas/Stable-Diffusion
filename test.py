from tqdm import tqdm
import time
import torch

n = 1
x = torch.randn((n, 3, 64, 64))

# print(x)

for i in tqdm(reversed(range(1, 5)), position=0):
    print(i)
    t = (torch.ones(n) * i).long()
    # print(t)
    
    if i > 1:
        noise = torch.randn_like(x)
        # print(f"This is if i > 1 {noise}")
    else:
        noise = torch.zeros_like(x)
        # print(f"This is else {noise}")