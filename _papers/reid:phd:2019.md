---
ENTRYTYPE: phdthesis
abstract: 'One of the most important interfaces in a computer system is the interface between hardware and software.  This interface is the contract between
  the hardware designer and the programmer that defines the functional behaviour of the hardware.  This thesis examines two critical aspects of defining
  the hardware-software interface: quality and performance.  The first aspect is creating a high quality specification of the interface as conventionally
  defined in an instruction set architecture.  The majority of this thesis is concerned with creating a specification that covers the full scope of the
  interface; that is applicable to all current implementations of the architecture; and that can be trusted to accurately describe the behaviour of implementations
  of the architecture.  We describe the development of a formal specification of the two major types of Arm processors: A-class (for mobile devices such
  as phones and tablets) and M-class (for micro-controllers). These specifications are unparalleled in their scope, applicability and trustworthiness.  This
  thesis identifies and illustrates what we consider the key ingredient in achieving this goal: creating a specification that is used by many different
  user groups.  Supporting many different groups leads to improved quality as each group finds different problems in the specification; and, by providing
  value to each different group, it helps justify the considerable effort required to create a high quality specification of a major processor architecture.  The
  work described in this thesis led to a step change in Arm''s ability to use formal verification techniques to detect errors in their processors; enabled
  extensive testing of the specification against Arm''s official architecture conformance suite; improved the quality of Arm''s architecture conformance
  suite based on measuring the architectural coverage of the tests; supported earlier, faster development of architecture extensions by enabling animation
  of changes as they are being made; and enabled early detection of problems created from architecture extensions by performing formal validation of the
  specification against semi-structured natural language specifications.  As far as we are aware, no other mainstream processor architecture has this capability.  The
  formal specifications are included in Arm''s publicly released architecture reference manuals and the A-class specification is also released in machine-readable
  form.  The second aspect is creating a high performance interface by defining the hardware-software interface of a software-defined radio subsystem using
  a programming language.  That is, an interface that allows software to exploit the potential performance of the underlying hardware.  While the hardware-software
  interface is normally defined in terms of machine code, peripheral control registers and memory maps, we define it using a programming language instead.  This
  higher level interface provides the opportunity for compilers to hide some of the low-level differences between different systems from the programmer:
  a potentially very efficient way of providing a stable, portable interface without having to add hardware to provide portability between different hardware
  platforms.  We describe the design and implementation of a set of extensions to the C programming language to support programming high performance, energy
  efficient, software defined radio systems. The language extensions enable the programmer to exploit the pipeline parallelism typically present in digital
  signal processing applications and to make efficient use of the asymmetric multiprocessor systems designed to support such applications.  The extensions
  consist primarily of annotations that can be checked for consistency and that support annotation inference in order to reduce the number of annotations
  required.  Reducing the number of annotations does not just save programmer effort, it also improves portability by reducing the number of annotations
  that need to be changed when porting an application from one platform to another.  This work formed part of a project that developed a high-performance,
  energy-efficient, software defined radio capable of implementing the physical layers of the 4G cellphone standard (LTE), 802.11a WiFi and Digital Video
  Broadcast (DVB) with a power and silicon area budget that was competitive with a conventional custom ASIC solution.  The Arm architecture is the largest
  computer architecture by volume in the world.  It behooves us to ensure that the interface it describes is appropriately defined.'
added: 2019-06-01
affiliation: School of Computing Science, University of Glasgow
ar_shortname: PhD 19
authors:
- Alastair D. Reid
layout: paper
location: Glasgow, Scotland
month: March
numpages: '161'
read: false
readings: []
school: School of Computing Science, University of Glasgow
title: 'Defining interfaces between hardware and software: Quality and performance'
year: 2019
url: http://theses.gla.ac.uk/41068/
notes:
- ASL
- Arm architecture
- ISA specification
- instruction set architecture
- CPU verification
- model checking
- bounded model checking
- RTL
- requirements specification
- remote procedure call
- pipeline parallelism
- continuations
- threads
- decoupling
- SIMD
- vector architecture
papers:
- reid:fmcad:2016
- reid:cav:2016
- reid:oopsla:2017
- reid:cases:2008
---

{% include links.html %}
