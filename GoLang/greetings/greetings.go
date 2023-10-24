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
	formats := []string{ //This is known as a "slice"
		"Hi, %v. Welcome!",
		"Great to see you, %v!",
		"Hail, %v! Well met!",
	}

	//Return a randomly selected message by specifying a random index for the slice of formats.
	return formats[rand.Intn(len(formats))]
}

//Hellos returns a map that associates each of the named people with a greeting message
func Hellos(names []string) (map[string]string, error) { //In Go you initialize a map with map[<key type>]<value type>
	//A map to associate name with messages.
	messages := make(map[string]string)
	//Loop through the recieved slice of names, calling the Hello function to get a message for each name.
	for _, name := range names {
		message, err := Hello(name)
		if err != nil {
			return nil, err
		}
		//In the map, associate the retrieved message with the name
		messages[name] = message
	}
	return messages, nil
}