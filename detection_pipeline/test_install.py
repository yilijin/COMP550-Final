from mmdet.apis import init_detector, inference_detector

config_file = './detection_pipeline/config.py'
checkpoint_file = './detection_pipeline/epoch_1.pth'
model = init_detector(config_file, checkpoint_file, device='cpu')  # or device='cuda:0'

print(inference_detector(model, './demo/demo_img.jpg'))