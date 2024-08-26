def readFile(fileName) {
    println("fileName: $fileName")
    return 'sample text'
}

def readJSON(fileName) {
    println("fileName: $fileName")
    return [sample: 'text']
}

return this
