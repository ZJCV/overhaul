<div align="right">
  Language:
    🇺🇸
  <a title="Chinese" href="./README.zh-CN.md">🇨🇳</a>
</div>

 <div align="center"><a title="" href="https://github.com/ZJCV/overhaul.git"><img align="center" src="./imgs/overhaul.png"></a></div>

<p align="center">
  «overhaul» re-implements the paper <a title="" href="https://arxiv.org/abs/1904.01866">A Comprehensive Overhaul of Feature Distillation</a>
<br>
<br>
  <a href="https://github.com/RichardLitt/standard-readme"><img src="https://img.shields.io/badge/standard--readme-OK-green.svg?style=flat-square"></a>
  <a href="https://conventionalcommits.org"><img src="https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg"></a>
  <a href="http://commitizen.github.io/cz-cli/"><img src="https://img.shields.io/badge/commitizen-friendly-brightgreen.svg"></a>
</p>

|     arch_s    |  top1  |  top5  |     arch_t    |  top1  |  top5  |  dataset | lambda |  top1  |  top5  |
|:-----------:|:------:|:------:|:-------------:|:------:|:------:|:--------:|:------:|:------:|:------:|
| MobileNetv2 | 79.420 | 95.680 |    ResNet50   | 83.290 | 96.630 | CIFAR100 |  15.0  | 82.440 | 96.540 |
|   ResNet18  | 80.720 | 95.840 |    ResNet50   | 83.290 | 96.630 | CIFAR100 |   2.0  | 82.470 | 96.360 |
|   ResNet18  | 80.720 | 95.840 |   ResNet152   | 85.660 | 97.590 | CIFAR100 |   2.0  | 83.310 | 97.000 |
|   ResNet50  | 83.290 | 96.630 |   ResNet152   | 85.660 | 97.590 | CIFAR100 |   2.0  | 86.080 | 97.350 |
|   ResNet50  | 83.290 | 96.630 | ResNeXt_32x8d | 85.600 | 97.460 | CIFAR100 |   2.0  | 85.410 | 97.430 |

more see [docs](./docs/README.md)

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Background](#background)
- [Installation](#installation)
- [Usage](#usage)
- [Maintainers](#maintainers)
- [Thanks](#thanks)
- [Contributing](#contributing)
- [License](#license)

## Background

According to choose new distillation position and design new teacher transfer and distance function, the OFD (Overhaul of Feature Distillation) realizes the better distillation improvement.

Current project implementation is based on [ clovaai/overhaul-distillation](https://github.com/clovaai/overhaul-distillation).

## Installation

```
$ pip install -r requirements.txt
```

## Usage

* Train

```angular2html
$ CUDA_VISIBLE_DEVICES=0 python tools/train.py -cfg=configs/resnet/ofd_2_0_r50_pret_r18_c100_224_e100_sgd_mslr.yaml
```

* Test

```angular2html
$ CUDA_VISIBLE_DEVICES=0 python tools/test.py -cfg=configs/resnet/ofd_2_0_r50_pret_r18_c100_224_e100_sgd_mslr.yaml
```

## Maintainers

* zhujian - *Initial work* - [zjykzj](https://github.com/zjykzj)

## Thanks

```
@inproceedings{heo2019overhaul,
  title={A Comprehensive Overhaul of Feature Distillation},
  author={Heo, Byeongho and Kim, Jeesoo and Yun, Sangdoo and Park, Hyojin and Kwak, Nojun and Choi, Jin Young},
  booktitle = {International Conference on Computer Vision (ICCV)},
  year={2019}
}
```

## Contributing

Anyone's participation is welcome! Open an [issue](https://github.com/ZJCV/overhaul/issues) or submit PRs.

Small note:

* Git submission specifications should be complied
  with [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0-beta.4/)
* If versioned, please conform to the [Semantic Versioning 2.0.0](https://semver.org) specification
* If editing the README, please conform to the [standard-readme](https://github.com/RichardLitt/standard-readme)
  specification.

## License

[Apache License 2.0](LICENSE) © 2021 zjykzj