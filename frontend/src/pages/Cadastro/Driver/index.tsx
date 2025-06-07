import { RegInput } from "@components/InputForm";
import { zodResolver } from "@hookform/resolvers/zod";
import {
  driverRegisterFormSchema,
  type IDriverRegisterData,
} from "@schemas/driverRegisterSchema";
import { useForm, type FieldError, type SubmitHandler } from "react-hook-form";
import { RegisterPageGeneric } from "@components/RegisterForm";
import { Button } from "@styles/Buttons";
import { SelectInputForm } from "@components/Select";
import { cnhCategories } from "@utils/Selects/cnhCategories";
import { Sidebar } from "@components/Sidebar";
import { ContainerInputs, Section } from "./styles";
import { useState } from "react";
import { useDriver } from "@hooks/useDriver";

const DriverRegister = () => {
  const [inputValue, setInputValue] = useState("");
  const [inputDate, setInputDate] = useState("");
  const { handleCreateDriver } = useDriver();

  const cpfMask = (value: string) => {
    return value
      .replace(/\D/g, "")
      .replace(/(\d{3})(\d)/, "$1.$2")
      .replace(/(\d{3})(\d)/, "$1.$2")
      .replace(/(\d{3})(\d{1,2})/, "$1-$2")
      .replace(/(-\d{2})\d+?$/, "$1");
  };

  const dateMask = (value: string) => {
    return value
      .replace(/\D/g, "")
      .replace(/^(\d{2})(\d)/, "$1/$2")
      .replace(/^(\d{2})\/(\d{2})(\d)/, "$1/$2/$3")
      .slice(0, 10);
  };

  const handleInputMask = (event: React.ChangeEvent<HTMLInputElement>) => {
    setInputValue(cpfMask(event.target.value));
  };

  const handleDateMask = (event: React.ChangeEvent<HTMLInputElement>) => {
    setInputDate(dateMask(event.target.value));
  };

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm({
    resolver: zodResolver(driverRegisterFormSchema),
  });

  const submitDriver: SubmitHandler<IDriverRegisterData> = async (
    registerForm: IDriverRegisterData
  ) => {
    handleCreateDriver(registerForm);
  };

  return (
    <Section>
      <Sidebar />
      <RegisterPageGeneric title="Cadastro de motorista">
        <form onSubmit={handleSubmit(submitDriver)}>
          <ContainerInputs>
            <RegInput
              type={"text"}
              placeholder={"Digite o nome do motorista"}
              id={"nome"}
              label={"Nome"}
              {...register("name")}
              error={errors.name}
            />
            <RegInput
              type={"text"}
              placeholder={"999.999.99-99"}
              id={"cpf"}
              label={"CPF"}
              {...register("cpf")}
              error={errors.cpf}
              value={inputValue}
              onChange={handleInputMask}
            />
            <RegInput
              type={"email"}
              placeholder={"motorista@mail.com.br"}
              id={"email"}
              label={"Email"}
              {...register("email")}
              error={errors.email}
            />
            <SelectInputForm
              optionsArray={cnhCategories}
              label={"Carteira de Habilitaçao"}
              {...register("licenceType")}
              error={errors.licenceType}
            />
            <RegInput
              type={"number"}
              placeholder={"Numero da habilitação"}
              id={"licenceNumber"}
              label={"Número CNH"}
              {...register("licenceNumber")}
              error={errors.licenceNumber}
            />
            <RegInput
              type={"number"}
              placeholder={"Ex: 5"}
              id={"performance"}
              label={"Aproveitamento"}
              {...register("performance", { valueAsNumber: true })}
              error={errors.performance as FieldError}
            />
            <RegInput
              type={"text"}
              placeholder={"Data de nascimento"}
              id={"birthYear"}
              label={"Data de nascimento"}
              {...register("birthYear")}
              error={errors.birthYear}
              value={inputDate}
              onChange={handleDateMask}
            />
            <RegInput
              type={"password"}
              placeholder={"Digite a senha do motorista"}
              id={"password"}
              label={"Senha"}
              {...register("password")}
              error={errors.password}
            />
          </ContainerInputs>
          <div className="form__sendButton">
            <Button>ENVIAR</Button>
          </div>
        </form>
      </RegisterPageGeneric>
    </Section>
  );
};

export { DriverRegister };
