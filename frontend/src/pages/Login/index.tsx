import { useForm, Controller } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { z } from "zod";
import { useNavigate } from "react-router-dom";
import {
  Container,
  LeftContainer,
  RightContainer,
  TitleDiv,
  Links,
  BotaoEntrar,
  ConainerLift,
} from "./Styles";
import { toast } from "react-toastify";
// import { api } from "../../services/api";
import Logo from "@assets/Logo.png";
import { InputComponent } from "@components/Input";

const schema = z
  .object({
    cpf: z
      .string({ required_error: "CPF é obrigatório" })
      .min(14, "CPF Inválido"),
    password: z
      .string({ required_error: "Senha é obrigatória" })
      .min(6, "A senha precisa ter no mínimo 6 caracteres"),
  })
  .required();

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
    resolver: zodResolver(schema),
  });

  const onSubmit = (data: FormData) => {
    console.log("Dadus enviados:", data);
    toast.success("Login enviado com sucesso!");
    setTimeout(() => {
      navigate("/");
    }, 2000);
  };

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
