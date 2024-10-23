package main

import (
	"math/rand"
	"sync"
	"time"
)

var pokemonList = []string{
	// "Pikachu",
	"Charmander",
	"Squirtle",
	"Bulbasaur",
	"Jigglypuff",
}
var cond = sync.NewCond(&sync.Mutex{})
var pokemon = ""

func main() {
	// Consumer
	go func() {
		cond.L.Lock()
		defer cond.L.Unlock()

		// waits until Pikachu appears
		for pokemon != "Pikachu" {
			cond.Wait()
		}
		println("Caught " + pokemon)
		pokemon = ""
	}()

	// Producer
	go func() {
		// Every 1ms, a random Pokémon appears
		for i := 0; i < 100; i++ {
			time.Sleep(time.Millisecond)

			cond.L.Lock()
			pokemon = pokemonList[rand.Intn(len(pokemonList))]
			cond.L.Unlock()

			cond.Signal()
		}
	}()

	time.Sleep(100 * time.Millisecond) // lazy wait
}

// Output:
// Caught Pikachu
