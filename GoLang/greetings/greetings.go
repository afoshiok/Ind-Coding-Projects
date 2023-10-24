package greetings

import (
	"errors"
	"fmt"
)

//Hello returns a greeting for the named person.
func Hello(name string) (string, error) { //function pattern: func Name(var_Name <type>) <return type>
	//If no name was given, return an error with a message.
	if name == ""{
		return "", errors.New("empty name")
	}

	//If a name was recieved,
	//Return a greeting that embeds the name in a message.
	var message string
	message = fmt.Sprintf("Hello my name is %v", name)
	return message, nil
}