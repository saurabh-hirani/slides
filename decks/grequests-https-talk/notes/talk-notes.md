### Talk notes

### Intro

- We help our customers design and make things. From skyscrapers to smart cars, from buildings to blockbuster movies.
  We have varied range of products which enable customers from designing in the digital world to making them in the real world.
  With a lot of products come a lot of APIs. And with a lot APIs come a lot of monitoring metrics. This talk is about some
  interesting scenarios we ran into while trying to gather monitoring metrics concurrently in Python.

#### Slide-1

- I am working with the Site Reliability Engineering team at Autodesk
- I am going to present some interesting scenarios I ran into when doing a very simple task in
  Python - making concurrent HTTPS GET requests
- Before we go ahead - let me address a very important question

#### Slide-2

- What's in it for you? Why should you attend this talk?
- First of all we will go through a very entertaining, hands on debugging story
- A peek under the hood of grequests and gevent internals - both of which are widely used libraries in Python
- Along the way we will look at profiling and tracing your code which will show us some interesting numbers.
- We will also answer a very important question.

#### Slide-3

- What was the use case that led to the problem?
- I did not even bother debugging the problem because Python2.7 support is ending Jan 2020
- But life's not that simple.
- I had to root cause out why Python2.7 is running slow with HTTPS

#### Slide-5

- We have a reporting tool which does 10,000+ HTTPS GET to internal and third party services.
- Gets the data, crunches some numbers and dumps the data

#### Slide-6

- AWS Lambda is a function-as-a-service offering by AWS - which allows you to run your code without
  bothering about the underlying infra.

#### Slide-8

- We will look at grequests lib in detail but we need to know the following for now
- requests module uses a blocking socket - which means that if I have to do a GET on 2 URLs
- This is an extremely simplified view - we will look at this in more detail as we go along

#### Slide-9

- Both the servers are powered by go-httpbin which is the golang equivalent of httpbin.org

#### Slide-10

- Let's see some code in action - we are at stage-0 - we are trying out grequests for the first time.
