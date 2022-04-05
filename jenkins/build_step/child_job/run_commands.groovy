def run(test_config) {
  if (test_config.b) {
    echo "b: ${test_config.b}"
  }
}

return [
  run: this.&run
]
