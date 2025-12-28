package main

import (
	"fault_tolerance/internal/handler"
	"fault_tolerance/internal/store"
	"log"
	"net/http"
	"os"
)

/*
read PORT, NODE_ID, ROLE, DB_URL from env

make a store object

make a router (http.NewServeMux())

register /health handler

call ListenAndServe(":"+PORT, mux)
*/

func get_env(key string) string {
	variable := os.Getenv(key)
	if variable != "" {
		log.Printf("env file not opened sucessfully")
	}
	return variable
}

func main() {
	nodeID := get_env("NODE_ID")
	port := get_env("PORT")
	role := get_env("ROLE")
	dbURL := get_env("DB_URL")
	mux := http.NewServeMux()
	st, err := store.New(dbURL)
	if err != nil {
		log.Fatalf("failed to create store %v", err)
	}

	defer st.Close()
	mux.Handle("/health", handler.Health(nodeID, role, st))
	addr := ":" + port
	log.Printf("node %s (%s) listening on %s", nodeID, role, addr)
	log.Fatal(http.ListenAndServe(addr, mux))

}
