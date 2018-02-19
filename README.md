# Stock Clustering

Welcome to my little Stock Analysis/Clustering. The goal here is to find patterns in stock data (price history) and compare them to their GICS classification. Therefore unsupervised learning algorithms are applied to the raw and/or pre-processed data. Beneath you can find a table with the current results, showing information about the algorithms used and scores when the results are run against the GICS classes.

Furthermore I'll add some thoughts on the results, my progress and what may be next as I move on, to keep you updated and as my own little roadmap. If you're interested you can find the current PDF file with more information in the latex folder. As this is work in progress, the results may not look pretty right now but I may come to that, in case the results are good enough. In case you have any suggestions on what to improve, I'd be happy if you hit me up.

Python packages used right now:
  - pandas
  - numpy
  - scikit-learn
  - scipy

### Current Results

Dillinger is currently extended with the following plugins. Instructions on how to use them in your own application are linked below.

| index | preparation          |         | algorithm     | distance  | results                  |        |          |        |        |             |              |           |        |          |
|-------|----------------------|---------|---------------|-----------|--------------------------|--------|----------|--------|--------|-------------|--------------|-----------|--------|----------|
|       | offset & amplitude | detrend |               |           | chi square   contingency |        | G-Test   |        | ADI    | homogeneity | completeness | v_measure | AMI    | FM score |
|       |                      |         |               |           | X^2                      | p-val  | G        | p-val  |        |             |              |           |        |          |
| 1     | no                   | no      | k-means       | euclidean | 113.5868                 | 0.1668 | 116.1262 | 0.1291 | 0.0029 | 0.0518      | 0.0646       | 0.0575    | 0.0117 | 0.1499   |
| 2     | yes                  | no      | k-means       | euclidean | 274.8038                 | 0.0000 | 276.2700 | 0.0000 | 0.0368 | 0.1232      | 0.1271       | 0.1251    | 0.0791 | 0.1593   |
| 3     | yes                  | yes     | k-means       | euclidean | 426.6852                 | 0.0000 | 361.6610 | 0.0000 | 0.0588 | 0.1613      | 0.1617       | 0.1615    | 0.1192 | 0.1710   |
| 4     | no                   | no      | agglomerative | euclidean | 111.0553                 | 0.2115 | 115.0035 | 0.1449 | 0.0047 | 0.0513      | 0.0685       | 0.0587    | 0.0116 | 0.1666   |
| 5     | yes                  | no      | agglomerative | euclidean | 318.3593                 | 0.0000 | 327.7027 | 0.0000 | 0.0494 | 0.1461      | 0.1496       | 0.1479    | 0.1036 | 0.1633   |
| 6     | yes                  | yes     | agglomerative | euclidean | 472.0161                 | 0.0000 | 395.4873 | 0.0000 | 0.0605 | 0.1764      | 0.1794       | 0.1779    | 0.1352 | 0.1737   |

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;}
.tg th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;}
.tg .tg-s6z2{text-align:center}
.tg .tg-baqh{text-align:center;vertical-align:top}
.tg .tg-yw4l{vertical-align:top}
</style>
<table class="tg">
  <tr>
    <th class="tg-s6z2" rowspan="3">index</th>
    <th class="tg-s6z2" colspan="2">preparation</th>
    <th class="tg-s6z2" rowspan="3">algorithm</th>
    <th class="tg-s6z2" rowspan="3">distance</th>
    <th class="tg-s6z2" colspan="10">results</th>
  </tr>
  <tr>
    <td class="tg-s6z2" rowspan="2">offset &amp;<br>  amplitude</td>
    <td class="tg-s6z2" rowspan="2">detrend</td>
    <td class="tg-s6z2" colspan="2">chi square<br>  contingency</td>
    <td class="tg-s6z2" colspan="2">G-Test</td>
    <td class="tg-s6z2" rowspan="2">ADI</td>
    <td class="tg-s6z2" rowspan="2">homogeneity</td>
    <td class="tg-s6z2" rowspan="2">completeness</td>
    <td class="tg-s6z2" rowspan="2">v measure</td>
    <td class="tg-s6z2" rowspan="2">AMI</td>
    <td class="tg-baqh" rowspan="2">FM score</td>
  </tr>
  <tr>
    <td class="tg-s6z2">X^2</td>
    <td class="tg-s6z2">p-val</td>
    <td class="tg-s6z2">G</td>
    <td class="tg-s6z2">p-val</td>
  </tr>
  <tr>
    <td class="tg-031e">1</td>
    <td class="tg-031e">no</td>
    <td class="tg-031e">no</td>
    <td class="tg-031e">k-means</td>
    <td class="tg-031e">euclidean</td>
    <td class="tg-031e">113.5868</td>
    <td class="tg-031e">0.1668</td>
    <td class="tg-031e">116.1262</td>
    <td class="tg-031e">0.1291</td>
    <td class="tg-031e">0.0029</td>
    <td class="tg-031e">0.0518</td>
    <td class="tg-031e">0.0646</td>
    <td class="tg-031e">0.0575</td>
    <td class="tg-031e">0.0117</td>
    <td class="tg-yw4l">0.1499</td>
  </tr>
  <tr>
    <td class="tg-031e">2</td>
    <td class="tg-031e">yes</td>
    <td class="tg-031e">no</td>
    <td class="tg-031e">k-means</td>
    <td class="tg-031e">euclidean</td>
    <td class="tg-031e">274.8038</td>
    <td class="tg-031e">0.0000</td>
    <td class="tg-031e">276.2700</td>
    <td class="tg-031e">0.0000</td>
    <td class="tg-031e">0.0368</td>
    <td class="tg-031e">0.1232</td>
    <td class="tg-031e">0.1271</td>
    <td class="tg-031e">0.1251</td>
    <td class="tg-031e">0.0791</td>
    <td class="tg-yw4l">0.1593</td>
  </tr>
  <tr>
    <td class="tg-031e">3</td>
    <td class="tg-031e">yes</td>
    <td class="tg-031e">yes</td>
    <td class="tg-031e">k-means</td>
    <td class="tg-031e">euclidean</td>
    <td class="tg-031e">426.6852</td>
    <td class="tg-031e">0.0000</td>
    <td class="tg-031e">361.6610</td>
    <td class="tg-031e">0.0000</td>
    <td class="tg-031e">0.0588</td>
    <td class="tg-031e">0.1613</td>
    <td class="tg-031e">0.1617</td>
    <td class="tg-031e">0.1615</td>
    <td class="tg-031e">0.1192</td>
    <td class="tg-yw4l">0.1710</td>
  </tr>
  <tr>
    <td class="tg-031e">4</td>
    <td class="tg-031e">no</td>
    <td class="tg-031e">no</td>
    <td class="tg-031e">agglomerative</td>
    <td class="tg-031e">euclidean</td>
    <td class="tg-031e">111.0553</td>
    <td class="tg-031e">0.2115</td>
    <td class="tg-031e">115.0035</td>
    <td class="tg-031e">0.1449</td>
    <td class="tg-031e">0.0047</td>
    <td class="tg-031e">0.0513</td>
    <td class="tg-031e">0.0685</td>
    <td class="tg-031e">0.0587</td>
    <td class="tg-031e">0.0116</td>
    <td class="tg-yw4l">0.1666</td>
  </tr>
  <tr>
    <td class="tg-031e">5</td>
    <td class="tg-031e">yes</td>
    <td class="tg-031e">no</td>
    <td class="tg-031e">agglomerative</td>
    <td class="tg-031e">euclidean</td>
    <td class="tg-031e">318.3593</td>
    <td class="tg-031e">0.0000</td>
    <td class="tg-031e">327.7027</td>
    <td class="tg-031e">0.0000</td>
    <td class="tg-031e">0.0494</td>
    <td class="tg-031e">0.1461</td>
    <td class="tg-031e">0.1496</td>
    <td class="tg-031e">0.1479</td>
    <td class="tg-031e">0.1036</td>
    <td class="tg-yw4l">0.1633</td>
  </tr>
  <tr>
    <td class="tg-yw4l">6</td>
    <td class="tg-yw4l">yes</td>
    <td class="tg-yw4l">yes</td>
    <td class="tg-yw4l">agglomerative</td>
    <td class="tg-yw4l">euclidean</td>
    <td class="tg-yw4l">472.0161</td>
    <td class="tg-yw4l">0.0000</td>
    <td class="tg-yw4l">395.4873</td>
    <td class="tg-yw4l">0.0000</td>
    <td class="tg-yw4l">0.0605</td>
    <td class="tg-yw4l">0.1764</td>
    <td class="tg-yw4l">0.1794</td>
    <td class="tg-yw4l">0.1779</td>
    <td class="tg-yw4l">0.1352</td>
    <td class="tg-yw4l">0.1737</td>
  </tr>
</table>
