[![N|Solid](http://www.thucydides.info/img/serenity-bdd.png)](http://www.thucydides.info/#/)

# Serenity BDD
This project shows Serenity framework integration to run sample test case for Belcorp.


# Setting up
To run this tutorial, you will need [JDK 8](https://www.oracle.com/java/technologies/javase-jdk8-downloads.html), [Maven](https://maven.apache.org/) and [Git](https://git-scm.com/downloads).

Java IDE:
* [IntelliJ IDE](https://www.jetbrains.com/idea/download/) (you can use the free Community Edition)
* [Eclipse IDE](https://www.eclipse.org/downloads/)

> Make sure that the bundled Cucumber for Java plugin is enabled.

Now clone this project to your local machine:

```sh
$ git clone https://github.com/elionavarretev/SerenityBDD-Belcorp.git
```

# Building the project
This project uses a Maven build. To run the tests and build an executable jar, open the terminal and run:

```sh
$ mvn install
```

The first time you run this it may take some time to download the dependencies.

# How To Run From Command Line

```sh
$ mvn verify serenity:aggregate -e -Dwebdriver.driver=chrome
```

# Note:
Please run and review the code
If you think something needs to be improved; you can indicate the file issue or submit PR.


