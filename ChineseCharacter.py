import torch

ckpt1 = torch.load('/hy-tmp/project/runs/train/exp/weights/last.pt')

ckpt1['model'].names = ['transverse cracks',' longitudinal cracks', 'massive cracks',' crack ', 'pit slot', 'repair mesh cracks',' to repair the cracks', 'repair pit slot']
 
torch.save(ckpt1, '/hy-tmp/project/runs/train/exp/weights/last.pt')