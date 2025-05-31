import { useForm, Controller } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { useNavigate } from "react-router-dom";
import { toast } from "react-toastify";
import { api } from "@services/api";
import { Loginschema } from '@schemas/LoginSchema';
import Logo from "@assets/Logo.png";
import { InputComponent } from "@components/Input";
import { ClearMask } from '@utils/Mask/ClearMask'
import {
    Container,
    LeftContainer,
    RightContainer,
    TitleDiv,
    Links,
    BotaoEntrar,
    ConainerLift,
} from "./Styles";


type FormData = {
    cpf: string;
    password: string;
};

export function Login() {
  const navigate = useNavigate();
  const {
      control,
      handleSubmit,
      formState: { errors },
  } = useForm<FormData>({
      resolver: zodResolver(Loginschema),
  });

  const onSubmit = async (data: FormData) => {
      const cpf = ClearMask(data.cpf)
      console.log(cpf)
      const reponse = await toast.promise(
          api.post('/login', {
              cpf: cpf,
              password: data.password
          }),
          {
              pending:"Verificando login",
              success: {
                  render(){
                      setTimeout(() => {
                          navigate("/home")
                      }, 2000);
                      return "Seja bem vindo!"
                  }
              },
              error: "CPF ou senha está incorreto"
          }
      )
      localStorage.clear()
      localStorage.setItem("nome", reponse.data.nome)
  }

  return (
    <Container>
        <LeftContainer>
            <ConainerLift>
                <TitleDiv>
                    <img src={Logo} alt="Logo-Viação-União" />
                    <h1>
                      Viação <br />
                      <span>UNIÃO</span>
                    </h1>
                </TitleDiv>    
                <form onSubmit={handleSubmit(onSubmit)}>
                  <Controller
                    name="cpf"
                    control={control}
                    render={({ field }) => (
                      <InputComponent
                        LabelText="CPF"
                        text="Digite seu CPF"
                        type="text"
                        mask="cpf"
                        {...field}
                        inputRef={field.ref}
                      />
                    )}
                  />
                  <p>{errors?.cpf?.message}</p>    
                  <br />    
                  <Controller
                    name="password"
                    control={control}
                    render={({ field }) => (
                      <InputComponent
                        LabelText="SENHA"
                        text="Digite sua senha"
                        type="password"
                        cadeado={true}
                        {...field}
                        inputRef={field.ref}
                      />
                    )}
                  />
                  <p>{errors?.password?.message}</p>    
                  <Links>
                    <a href="">Esqueci minha senha</a>
                    <a href="">Cadastre-se</a>
                  </Links>    
                  <BotaoEntrar type="submit">ENTRAR</BotaoEntrar>
                </form>
            </ConainerLift>
        </LeftContainer>
        <RightContainer />
    </Container>
  );
}
