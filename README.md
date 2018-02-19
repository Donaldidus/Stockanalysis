# Stock Clustering

Welcome to my little Stock Analysis/Clustering. The goal here is to find patterns in stock data (price history) and compare them to their [GICS classification](https://en.wikipedia.org/wiki/Global_Industry_Classification_Standard). Therefore unsupervised learning algorithms are applied to the raw and/or pre-processed data. Beneath you can find a table with the current results, showing information about the algorithms used and scores when the results are run against the GICS classes.

Furthermore I'll add some thoughts on the results, my progress and what may be next as I move on, to keep you updated and as my own little roadmap. If you're interested you can find the current [PDF](../latex/main.pdf) file with more information in the latex folder. As this is work in progress the results may not look pretty right now, but I may get to that in case the results are good enough. If you have any suggestions on what to improve, I'd be happy if you hit me up.

## Thoughts on Results

### Done
The first results, when applying ML algorithms on the raw data, yielded in very bad results. The results even failed the statstic contingency test. Adjusting offset and amplitude of the stocks increased the results significantly. Removing the trend from the data further improved the results.

### Current Problems
Even tough the metrics displaying the performance against the GICS increased too, the results are far from satisfactory right now. E.g. the [Adjusted Rand Index](https://en.wikipedia.org/wiki/Rand_index#Adjusted_Rand_index) (ARI) is close to zero (best of now 0.06), which indicates that the cluster are somewhat not similar to the GICS sectors at all (positive 1 would be a perfect match). 

### Moving On
Moving on the goal is to improving the ARI score and the other metrics. Therefore it's necessary to determine why the score is so low. As both homogeneity and completeness score are similar, it's not clear what the problem is. Looking at the mean silhouette coefficient I noticed it's extremly low (close to zero), that would imply that either the euclidean distance measurement is not appropriate or the cluster algorithms applied are not able to seperate the data right. So next I'll look for different distance metrics and cluster algorithms.

## Current Results

<table class="tg">
  <tr>
    <th class="tg-s6z2" rowspan="3">index</th>
    <th class="tg-s6z2" colspan="2">preparation</th>
    <th class="tg-s6z2" rowspan="3">algorithm</th>
    <th class="tg-s6z2" rowspan="3">distance</th>
    <th class="tg-s6z2" colspan="10">metrics</th>
  </tr>
  <tr>
    <td class="tg-s6z2" rowspan="2">offset &amp;<br>  amplitude</td>
    <td class="tg-s6z2" rowspan="2">detrend</td>
    <td class="tg-s6z2" colspan="2">chi square<br>  contingency</td>
    <td class="tg-s6z2" colspan="2">G-Test</td>
    <td class="tg-s6z2" rowspan="2"><a href="https://en.wikipedia.org/wiki/Rand_index#Adjusted_Rand_index">ARI</a></td>
    <td class="tg-s6z2" rowspan="2">homogeneity</td>
    <td class="tg-s6z2" rowspan="2">completeness</td>
    <td class="tg-s6z2" rowspan="2">v_measure</td>
    <td class="tg-s6z2" rowspan="2">AMI</td>
    <td class="tg-baqh" rowspan="2">FM_score</td>
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

## TODO
  - Include silhouette coefficient values in the table


Python packages used right now:
  - pandas
  - numpy
  - scikit-learn
  - scipy
