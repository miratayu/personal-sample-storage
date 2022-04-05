# 実装中に出くわした事のメモ
jenkins の groovy では下記のような書き方は出来ない…
```
f = new File(logName)
f.eachLine{line->
  echo "line: ${line}"
}
```
まず `new` が標準では許可されていないので避けた方が良さそう  
`Scripts not permitted to use new java.io.File java.lang.String`

次にそもそも `File` は無いと言われる  
`No such DSL method 'File' found among steps [... List of commands that can be used ...]`

readJSONはデフォルトでは無いようなので下記のプラグインを入れないとエラーする  
Pipeline Utility Steps


## 上流・下流の作り方(Jenkinsパイプラインから別ジョブ呼び出す)
1. 上流・下流のjobをそれぞれ作成する。
2. 上流jobのJenkinsfileで [Pipeline: Build Step](https://www.jenkins.io/doc/pipeline/steps/pipeline-build-step/) をする。
   1. `job` には下流jobのjob名を入れる。
   2. `parameters` には `choice` が無いので `string` で入れる。
3. 上流jobを実行すると下流jobが動く！

### その他リンク
- [使ってみよう！Jenkins「Pipeline」](https://qiita.com/miyasakura_/items/9d9a8873c333cb9e9f43)
- [Jenkins Declarative Pipeline 〜whenを使い倒す！〜](https://qiita.com/AHA_oretama/items/00813a041dc22416c6e4)
