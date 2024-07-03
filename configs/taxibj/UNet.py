method = 'UNet'
in_channels = 8
out_ts = 4
out_ch = 2
depth = 2
wf = 8
padding = True
batch_norm = True
pos_emb = False
up_mode = 'upconv'
lr = 5e-4
batch_size = 16
drop_path = 0.1
root_dir = "7daysv4"
data_root = "7daysv4"
workers = 8
epochs = 150
sched = 'cosine'
perm = False
