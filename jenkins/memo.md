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
