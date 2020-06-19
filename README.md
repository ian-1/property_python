# Property Python

Property management program built using tKinter in Python.

## Background

Combining an old program I built to test tKinter with the functionality of two ruby based programs I built (property Setter and PM Templates).  

## To Use Program

in Command Prompt:

```
> python property_python.rb
```

## User Stories

As a Property Manager  
So I can repond to an Applicant  
I want to be able to see templates to send to Applicants

As a Property Manager  
So I can repond to an Applicant  
I want to select a template to send to an Applicant

As a Property Manager  
So I can respond to an Applicant on {X} issue  
I want to be able to access a specific template on {X} issue

{X}:

- Return holding deposit - offer not formally accepted
- Question date for a break clause
etc.

As a Property Manager  
So I can keep a record of Actions carried out  
I want to be able to record an action

As a Property Manager  
So I can see what Action I have added  
I want to be able to read last action

As a Property Manager  
So I can see past Actions  
I want to be able to show list of actions

As a System User  
So I can edit templates (and the path to get to them) in a simple and easy to understand way  
I want templates (and questions used to get to them) saved in simple files/folders that corespond to the 'tree' of questions that will be used to bring the user to the template 

## Domain Model

Objects | Messages
---|---
Property Manager |  
Applicant |  
Template | see_templates <br> select  
Action | record(user, message) <br> read_last(user) <br> show_list(user) 