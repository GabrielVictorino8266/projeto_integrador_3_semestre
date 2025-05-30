import { useEffect, useState } from "react";

type Usuario = {
    nome: string | null;
    cargo: string | null;
}

export function useUsuario(){
    const [user, setUser] = useState<Usuario | null>(null)
    
    useEffect( () => {
        localStorage.clear()
        localStorage.setItem("nome", "Andersonx")
        localStorage.setItem ("cargo", "teste")

        const requisicao = async () => {
            setTimeout(() =>{
                const teste: Usuario = {
                    nome: localStorage.getItem("nome"),
                    cargo: localStorage.getItem("cargo") 
                }
                setUser(teste)
            },1000)
        }

        requisicao();

    },[])

    return { user }
}
