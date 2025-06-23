import { RegInput } from "@components/InputForm";
import { zodResolver } from "@hookform/resolvers/zod";
import { driverRegisterFormSchema } from "@schemas/driverRegisterSchema";
import { useForm, type FieldError, type SubmitHandler } from "react-hook-form";
import { RegisterPageGeneric } from "@components/RegisterForm";
import { DarkBlueButton } from "@styles/Buttons";
import { SelectInputForm } from "@components/Select";
import { cnhCategories } from "@utils/Selects/cnhCategories";
import { ContainerInputs } from "./styles";
import { useDriver } from "@hooks/useDriver";
import { useState } from "react";
import type { ICreateDriverData } from "@interfaces/driver.interface";
import { cpfMask, dateMask, phoneMask } from "@utils/reserve";
import { FaUser } from "react-icons/fa";

const DriverRegister = () => {
  const { handleCreateDriver } = useDriver();
  const [phoneValue, setPhoneValue] = useState<string>("");
  const [cpfValue, setcpfValue] = useState<string>("");
  const [dateValue, setdateValue] = useState<string>("");

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm({
    resolver: zodResolver(driverRegisterFormSchema),
  });

  const submitDriver: SubmitHandler<ICreateDriverData> = async (
    registerForm: ICreateDriverData
  ) => {
    await handleCreateDriver(registerForm);
    console.log(registerForm);
  };

  return (
    <RegisterPageGeneric
      icon={<FaUser className="headerIcon" />}
      title="CADASTRO DE MOTORISTA"
    >
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
          <SelectInputForm
            optionsArray={cnhCategories}
            label={"Carteira de Habilitaçao"}
            {...register("licenseType")}
            error={errors.licenseType}
          />
          <RegInput
            type={"text"}
            placeholder={"123.456.789-00"}
            id={"cpf"}
            label={"CPF"}
            {...register("cpf")}
            error={errors.cpf}
            value={cpfValue}
            onChange={(event) => {
              setcpfValue(cpfMask(event.target.value));
            }}
          />
          <RegInput
            type={"number"}
            placeholder={"Numero da habilitação"}
            id={"licenceNumber"}
            label={"Número CNH"}
            {...register("licenseNumber")}
            error={errors.licenseNumber}
          />
          {/*           <RegInput
            type={"password"}
            placeholder={"Digite a senha do motorista"}
            id={"password"}
            label={"Senha"}
            {...register("password")}
            error={errors.password}
          /> */}
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
            placeholder={"(XX) XXXXX-XXXX"}
            id={"phone"}
            label={"Telefone"}
            {...register("phone")}
            error={errors.phone}
            value={phoneValue}
            onChange={(event) => {
              setPhoneValue(phoneMask(event.target.value));
            }}
          />
          <RegInput
            type={"text"}
            placeholder={"Data de nascimento"}
            id={"birthYear"}
            label={"Data de nascimento"}
            {...register("birthYear")}
            error={errors.birthYear}
            value={dateValue}
            onChange={(event) => {
              setdateValue(dateMask(event.target.value));
            }}
          />
        </ContainerInputs>
        <div className="form__sendButton">
          <DarkBlueButton>Confirmar</DarkBlueButton>
        </div>
      </form>
    </RegisterPageGeneric>
  );
};

export { DriverRegister };
