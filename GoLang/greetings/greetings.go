package greetings

import (
	"errors"
	"fmt"
	"math/rand"
)

//Hello returns a greeting for the named person.
func Hello(name string) (string, error) { //function pattern: func Name(var_Name <type>) <return type>
	//If no name was given, return an error with a message.
	if name == ""{
		return "", errors.New("empty name")
	}

	//If a name was recieved,
	//Return a greeting that embeds the name in a message.
	var message string // or you can use := for implied type
	message = fmt.Sprintf(randomFormat(), name)
	return message, nil
}

func randomFormat() string {
	//A slice of message format
	formats := []string{
		"Hi, %v. Welcome!",
		"Great to see you, %v!",
		"Hail, %v! Well met!",
	}

	//Return a randomly selected message by specifying a random index for the slice of formats.
	return formats[rand.Intn(len(formats))]
}