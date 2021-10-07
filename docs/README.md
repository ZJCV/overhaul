
# README

## Benchmark Model

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-baqh{text-align:center;vertical-align:top}
.tg .tg-c3ow{border-color:inherit;text-align:center;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-c3ow">arch</th>
    <th class="tg-c3ow">dataset</th>
    <th class="tg-c3ow">top1</th>
    <th class="tg-c3ow">top5</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-baqh">MobileNetv2</td>
    <td class="tg-baqh">CIFAR100</td>
    <td class="tg-baqh">79.420</td>
    <td class="tg-baqh">95.680</td>
  </tr>
  <tr>
    <td class="tg-c3ow">ResNet18</td>
    <td class="tg-c3ow">CIFAR100</td>
    <td class="tg-c3ow">80.720</td>
    <td class="tg-c3ow">95.840</td>
  </tr>
  <tr>
    <td class="tg-c3ow">ResNet50</td>
    <td class="tg-c3ow">CIFAR100</td>
    <td class="tg-c3ow">83.290</td>
    <td class="tg-c3ow">96.630</td>
  </tr>
  <tr>
    <td class="tg-c3ow">ResNet152</td>
    <td class="tg-c3ow">CIFAR100</td>
    <td class="tg-c3ow">85.660</td>
    <td class="tg-c3ow">97.590</td>
  </tr>
  <tr>
    <td class="tg-c3ow">ResNeXt101_32x8d</td>
    <td class="tg-c3ow">CIFAR100</td>
    <td class="tg-c3ow">85.600</td>
    <td class="tg-c3ow">97.460</td>
  </tr>
</tbody>
</table>

## Distillation

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-c3ow{border-color:inherit;text-align:center;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-c3ow">arch_s</th>
    <th class="tg-c3ow">arch_t</th>
    <th class="tg-c3ow">dataset</th>
    <th class="tg-c3ow">lambda</th>
    <th class="tg-c3ow">top1</th>
    <th class="tg-c3ow">top5</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-c3ow">MobileNetV2</td>
    <td class="tg-c3ow">ResNet50</td>
    <td class="tg-c3ow">CIFAR100</td>
    <td class="tg-c3ow">15.0</td>
    <td class="tg-c3ow">82.440</td>
    <td class="tg-c3ow">96.540</td>
  </tr>
  <tr>
    <td class="tg-c3ow">ResNet18</td>
    <td class="tg-c3ow">ResNet50</td>
    <td class="tg-c3ow">CIFAR100</td>
    <td class="tg-c3ow">2.0</td>
    <td class="tg-c3ow">82.470</td>
    <td class="tg-c3ow">96.360</td>
  </tr>
  <tr>
    <td class="tg-c3ow">ResNet18</td>
    <td class="tg-c3ow">ResNet152</td>
    <td class="tg-c3ow">CIFAR100</td>
    <td class="tg-c3ow">2.0</td>
    <td class="tg-c3ow">83.310</td>
    <td class="tg-c3ow">97.000</td>
  </tr>
  <tr>
    <td class="tg-c3ow">ResNet50</td>
    <td class="tg-c3ow">ResNet152</td>
    <td class="tg-c3ow">CIFAR100</td>
    <td class="tg-c3ow">2.0</td>
    <td class="tg-c3ow">86.080</td>
    <td class="tg-c3ow">97.350</td>
  </tr>
  <tr>
    <td class="tg-c3ow">ResNet50</td>
    <td class="tg-c3ow">ResNeXt_32x8d</td>
    <td class="tg-c3ow">CIFAR100</td>
    <td class="tg-c3ow">2.0</td>
    <td class="tg-c3ow">85.410</td>
    <td class="tg-c3ow">97.430</td>
  </tr>
</tbody>
</table>

## See

* [mobilenet](mobilenet.md)

* [resnet](resnet.md)