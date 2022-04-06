def util(target) {
  echo "target: ${target}"
  if (!target) {
    error "target is not set"
  }
}

return [
  util: this.&util
]
