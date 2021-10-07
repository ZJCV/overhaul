
# README

## Benchmark Model


|       arch       |  dataset |  top1  |  top5  |
|:----------------:|:--------:|:------:|:------:|
|    MobileNetv2   | CIFAR100 | 79.420 | 95.680 |
|     ResNet18     | CIFAR100 | 80.720 | 95.840 |
|     ResNet50     | CIFAR100 | 83.290 | 96.630 |
|     ResNet152    | CIFAR100 | 85.660 | 97.590 |
| ResNeXt101_32x8d | CIFAR100 | 85.600 | 97.460 |

## Distillation

|    arch_s   |     arch_t    |  dataset | lambda |  top1  |  top5  |
|:-----------:|:-------------:|:--------:|:------:|:------:|:------:|
| MobileNetV2 |    ResNet50   | CIFAR100 |  15.0  | 82.440 | 96.540 |
|   ResNet18  |    ResNet50   | CIFAR100 |   2.0  | 82.470 | 96.360 |
|   ResNet18  |   ResNet152   | CIFAR100 |   2.0  | 83.310 | 97.000 |
|   ResNet50  |   ResNet152   | CIFAR100 |   2.0  | 86.080 | 97.350 |
|   ResNet50  | ResNeXt_32x8d | CIFAR100 |   2.0  | 85.410 | 97.430 |

## See

* [mobilenet](mobilenet.md)

* [resnet](resnet.md)