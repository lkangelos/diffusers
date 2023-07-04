## launch.json settings

1. unconditional_image_generation
```"args": ["--train_data_dir", "../data/rice", "--resolution", "64", "--output_dir", "ddpm-cloud-644", "--train_batch_size", "16", "--num_epochs", "100", "--gradient_accumulation_steps", "1", "--learning_rate", "1e-4", "--lr_warmup_steps", "500", "--mixed_precision", "no"],```

2. text_to_image
```"args": ["--pretrained_model_name_or_path", "../checkpoints/stable-diffusion-v1-4", "--dataset_name", "../data/lambdalabs/pokemon-blip-captions", "--use_ema", "--resolution", "512", "--center_crop", "--random_flip", "--output_dir", "sd-pokemon-model", "--train_batch_size", "1", "--max_train_steps", "15000", "--gradient_accumulation_steps", "4", "--gradient_checkpointing", "--learning_rate", "1e-5", "--max_grad_norm=1", "--lr_scheduler", "constant", "--lr_warmup_steps", "0", "--mixed_precision", "fp16"],```

3. controlnet
```"args": ["--mixed_precision", "fp16", "--pretrained_model_name_or_path", "../checkpoints/stable-diffusion-v1-4", "--dataset_name", "../data/fusing/fill50k", "--resolution", "512", "--train_batch_size", "4", "--learning_rate", "1e-5"],```