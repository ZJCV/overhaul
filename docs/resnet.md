
# resnet

|  arch_s  |     arch_t    |  dataset | lambda |  top1  |  top5  |
|:--------:|:-------------:|:--------:|:------:|:------:|:------:|
| ResNet18 |    ResNet50   | CIFAR100 |   0.1  | 80.730 | 95.800 |
| ResNet18 |    ResNet50   | CIFAR100 |   1.0  | 81.800 | 96.350 |
| ResNet18 |    ResNet50   | CIFAR100 |   2.0  | 82.470 | 96.360 |
| ResNet18 |    ResNet50   | CIFAR100 |   3.0  | 82.230 | 96.580 |
| ResNet18 |    ResNet50   | CIFAR100 |   4.0  | 82.190 | 96.470 |
| ResNet18 |   ResNet152   | CIFAR100 |   2.0  | 83.310 | 97.000 |
| ResNet50 |   ResNet152   | CIFAR100 |   2.0  | 86.080 | 97.350 |
| ResNet50 | ResNeXt_32x8d | CIFAR100 |   2.0  | 85.410 | 97.430 |