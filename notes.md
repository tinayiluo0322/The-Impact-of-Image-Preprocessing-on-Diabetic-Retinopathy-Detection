execute below before TF model running:
``` bash
export PATH="${PATH}:/usr/local/nvidia/bin:/usr/local/cuda/bin"
```

To upload to s3
``` bash
aws s3  sync s3_uploads s3://ml-diabetic-retinopathy  
``` 
**Note**: don't forget to add to the destibation subfolder