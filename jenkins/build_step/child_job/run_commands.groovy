def run(test_config) {
  echo "test_config.b: ${test_config.b}"
  if (test_config.b) {
    echo "test_config.b: ${test_config.b}"
  }
}

return [
  run: this.&run
]
