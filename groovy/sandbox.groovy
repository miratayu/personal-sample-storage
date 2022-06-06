
class Example {
    static void sum(int a,int b) {
        int c = a+b
        println "Hello"
        println c
    }

    static void say(first,second) {
        if(!first) {
            println "first string is empty!"
            return
        }
        String result = "say!" + (first as java.lang.CharSequence) + (second as java.lang.CharSequence)
        println result
    }

    static void main(String[] args) {
        sum(10,5)
        // say("Hello", "World")
        say("ABC", "World")

        println "===== test eachFile ====="
        new File('.').eachFile { println it.name }
    }
}

Example.main()
