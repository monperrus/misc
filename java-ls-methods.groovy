#!/bin/bash
//usr/bin/groovy  -cp /home/martin/spoon-core-6.1.0-jar-with-dependencies.jar "$0" "$@"; exit $?
// outputs the list of functions of Java file passed as parameter together with a checksum of the method body
// written in Groovy, using Spoon <https://github.com/INRIA/spoon>
// author: Martin Monperrus

import spoon.reflect.declaration.CtMethod;
import spoon.Launcher;
import spoon.processing.AbstractProcessor;

class Lister extends AbstractProcessor<CtMethod> {
  List result=[]
  void process(CtMethod c) {
    result.add(c.getSignature()+" "+c.toString().hashCode());
  }
}

l = new Launcher()
l.addInputResource(args[0])
def proc = new Lister();
l.addProcessor(proc);
l.getEnvironment().setNoClasspath(true);
l.buildModel();
l.getModel().processWith(proc)
def content=""
for(s in proc.result){
  content+=s+"\n"
}

print content 
