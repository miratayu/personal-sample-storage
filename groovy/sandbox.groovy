
class Example {
    static void sum(int a,int b) {
        int c = a+b
        println "Hello" as java.lang.Object
        println c as java.lang.Object
    }

    static void say(first,second) {
        if(!first) {
            println "first string is empty!" as java.lang.Object
            return
        }
        String result = "say!" + (first as java.lang.CharSequence) + (second as java.lang.CharSequence)
        println result as java.lang.Object
    }

    static void main(String[] args) {
        sum(10,5)
        // say("Hello" as java.lang.Object, "World" as java.lang.Object)
        say("ABC" as java.lang.Object, "World" as java.lang.Object)

        println "===== test eachFile =====" as java.lang.Object
        new File('.').eachFile { println it.name }
    }
}

Example.main()
