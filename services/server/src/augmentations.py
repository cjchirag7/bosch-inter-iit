import albumentations as A
augmentations_dict = {
1: A.Blur,
2: A.ChannelDropout,
3: A.ChannelShuffle,
4: A.CLAHE,
5: A.CoarseDropout,
6: A.ColorJitter,
7: A.Cutout,
8: A.Downscale,
9: A.Emboss,
10: A.Equalize,
11: A.FancyPCA,
12: A.Flip,
13: A.FromFloat,
14: A.GaussianBlur,
15: A.GaussNoise,
16: A.GlassBlur,
17: A.GridDistortion,
18: A.GridDropout,
19: A.HorizontalFlip,
20: A.HueSaturationValue,
21: A.ImageCompression,
22: A.InvertImg,
23: A.ISONoise,
24: A.JpegCompression,
25: A.Lambda,
26: A.MaskDropout,
27: A.MedianBlur,
28: A.MotionBlur,
29: A.MultiplicativeNoise,
30: A.Normalize,
31: A.OpticalDistortion,
32: A.PadIfNeeded,
33: A.Posterize,
34: A.RandomBrightness,
35: A.RandomBrightnessContrast,
36: A.RandomContrast,
37: A.RandomFog,
38: A.RandomGamma,
39: A.RandomGridShuffle,
40: A.RandomRain,
41: A.RandomShadow,
42: A.RandomSnow,
43: A.RandomSunFlare,
44: A.RandomToneCurve,
45: A.RGBShift,
46: A.Sharpen,
47: A.Solarize,
48: A.Superpixels,
49: A.ToFloat,
50: A.ToGray,
51: A.ToSepia,
52: A.Transpose,
53: A.VerticalFlip,
55: A.CenterCrop,
56: A.Crop,
57: A.CropAndPad,
58: A.CropNonEmptyMaskIfExists,
59: A.RandomCrop,
60: A.RandomCropNearBBox,
61: A.RandomResizedCrop,
62: A.RandomSizedBBoxSafeCrop,
63: A.RandomSizedCrop,
64: A.LongestMaxSize,
65: A.RandomScale,
66: A.Resize,
67: A.SmallestMaxSize,
68: A.RandomRotate90,
69: A.Rotate,
70: A.ElasticTransform,
71: A.Perspective,
72: A.ShiftScaleRotate
}
