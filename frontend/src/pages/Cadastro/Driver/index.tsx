import { RegInput } from "@components/InputForm";
import { zodResolver } from "@hookform/resolvers/zod";
import {
  type IDriverRegisterData,
  driverRegisterFormSchema,
} from "@schemas/driverRegisterSchema";
import { useForm, type SubmitHandler } from "react-hook-form";
import { RegisterPageGeneric } from "@components/RegisterForm";
import { Button } from "@styles/Buttons";
import { SelectInputForm } from "@components/Select";
import { cnhCategories } from "@utils/cnhCategories";

const DriverRegister = () => {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<IDriverRegisterData>({
    resolver: zodResolver(driverRegisterFormSchema),
  });

  const submitDriver: SubmitHandler<IDriverRegisterData> = async (
    registerForm
  ) => {
    console.log(registerForm);
  };

  try {
    //requiscao aqui
  } catch {
    //erro e chamar toast para informar o erro retornado pela API.
  }

  return (
    <section>
      <RegisterPageGeneric>
        <form onSubmit={handleSubmit(submitDriver)}>
          <RegInput
            type={"text"}
            placeholder={"Digite o nome do motorista"}
            id={"nome"}
            label={"Nome"}
            {...register("name")}
            error={errors.name}
          />
          <SelectInputForm
            optionsArray={cnhCategories}
            label={"Carteira de Habilitaçao"}
            {...register("cnh")}
            error={errors.cnh}
          />
          <RegInput
            type={"text"}
            placeholder={"Digite o CPF do motorista"}
            id={"cpf"}
            label={"CPF"}
            {...register("cpf")}
            error={errors.cpf}
          />
          <RegInput
            type={"password"}
            placeholder={"Digite a senha do motorista"}
            id={"password"}
            label={"Senha"}
            {...register("password")}
            error={errors.password}
          />
          <div className="form__sendButton">
            <Button>ENVIAR</Button>
          </div>
        </form>
      </RegisterPageGeneric>
    </section>
  );
};

export { DriverRegister };
