<div align="right">
  语言:
    🇨🇳
  <a title="英语" href="./README.md">🇺🇸</a>
</div>

 <div align="center"><a title="" href="https://github.com/ZJCV/overhaul.git"><img align="center" src="./imgs/overhaul.png"></a></div>

<p align="center">
  «overhaul»复现了论文<a title="" href="https://arxiv.org/abs/1904.01866">A Comprehensive Overhaul of Feature Distillation</a>
<br>
<br>
  <a href="https://github.com/RichardLitt/standard-readme"><img src="https://img.shields.io/badge/standard--readme-OK-green.svg?style=flat-square"></a>
  <a href="https://conventionalcommits.org"><img src="https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg"></a>
  <a href="http://commitizen.github.io/cz-cli/"><img src="https://img.shields.io/badge/commitizen-friendly-brightgreen.svg"></a>
</p>

* 解析：[ A Comprehensive Overhaul of Feature Distillation](https://blog.zhujian.life/posts/229eefa5.html)

|     arch_s    |  top1  |  top5  |     arch_t    |  top1  |  top5  |  dataset | lambda |  top1  |  top5  |
|:-----------:|:------:|:------:|:-------------:|:------:|:------:|:--------:|:------:|:------:|:------:|
| MobileNetv2 | 79.420 | 95.680 |    ResNet50   | 83.290 | 96.630 | CIFAR100 |  15.0  | 82.440 | 96.540 |
|   ResNet18  | 80.720 | 95.840 |    ResNet50   | 83.290 | 96.630 | CIFAR100 |   2.0  | 82.470 | 96.360 |
|   ResNet18  | 80.720 | 95.840 |   ResNet152   | 85.660 | 97.590 | CIFAR100 |   2.0  | 83.310 | 97.000 |
|   ResNet50  | 83.290 | 96.630 |   ResNet152   | 85.660 | 97.590 | CIFAR100 |   2.0  | 86.080 | 97.350 |
|   ResNet50  | 83.290 | 96.630 | ResNeXt_32x8d | 85.600 | 97.460 | CIFAR100 |   2.0  | 85.410 | 97.430 |

更多内容参见[docs](./docs/README.md)

## 内容列表

- [内容列表](#内容列表)
- [背景](#背景)
- [安装](#安装)
- [用法](#用法)
- [主要维护人员](#主要维护人员)
- [致谢](#致谢)
- [参与贡献方式](#参与贡献方式)
- [许可证](#许可证)

## 背景

`OFD`设计了新的蒸馏位置、教师转换以及距离函数，实现了更好的性能增益。

当前实现基于[ clovaai/overhaul-distillation](https://github.com/clovaai/overhaul-distillation)。

## 安装

```
$ pip install -r requirements.txt
```

## 用法

* 训练

```angular2html
$ CUDA_VISIBLE_DEVICES=0 python tools/train.py -cfg=configs/resnet/ofd_2_0_r50_pret_r18_c100_224_e100_sgd_mslr.yaml
```

* 测试

```angular2html
$ CUDA_VISIBLE_DEVICES=0 python tools/test.py -cfg=configs/resnet/ofd_2_0_r50_pret_r18_c100_224_e100_sgd_mslr.yaml
```

## 主要维护人员

* zhujian - *Initial work* - [zjykzj](https://github.com/zjykzj)

## 致谢

```
@inproceedings{heo2019overhaul,
  title={A Comprehensive Overhaul of Feature Distillation},
  author={Heo, Byeongho and Kim, Jeesoo and Yun, Sangdoo and Park, Hyojin and Kwak, Nojun and Choi, Jin Young},
  booktitle = {International Conference on Computer Vision (ICCV)},
  year={2019}
}
```

## 参与贡献方式

欢迎任何人的参与！打开[issue](https://github.com/ZJCV/overhaul/issues)或提交合并请求。

注意:

* `GIT`提交，请遵守[Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0-beta.4/)规范
* 语义版本化，请遵守[Semantic Versioning 2.0.0](https://semver.org)规范
* `README`编写，请遵守[standard-readme](https://github.com/RichardLitt/standard-readme)规范

## 许可证

[Apache License 2.0](LICENSE) © 2021 zjykzj