def add_json_contents(contents) {
  def added_contents = [:]
  contents.each { key, value ->
    added_contents[key] = value['value']
  }
  return added_contents
}

return [
  add_json_contents: this.&add_json_contents
]
