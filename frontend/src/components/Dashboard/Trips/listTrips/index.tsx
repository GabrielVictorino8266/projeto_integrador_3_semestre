import { ContainerInputs } from "@components/Dashboard/Driver/CreateDriver/styles";
import { RegInput } from "@components/InputForm";
import { RegisterPageGeneric } from "@components/RegisterForm";
import { SelectInputForm } from "@components/Select";
import { zodResolver } from "@hookform/resolvers/zod";
import { tripCreateFormSchema } from "@schemas/tripCreateSchema";

const TripRegister = () => {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm({
    resolver: zodResolver(tripCreateFormSchema),
  });

  // CRIAR OS TIPOS DO FORMULÁRIO E FUNCAO DE CADASTRO.

  const submitDriver: SubmitHandler<ICreateDriverData> = async (
    registerForm: ICreateDriverData
  ) => {
    // handleCreateDriver(registerForm);
    console.log(registerForm);
  };

  return (
    <RegisterPageGeneric title={"CADASTRO DE VIAGEM"}>
      <form onSubmit={handleSubmit(submitDriver)}>
        <ContainerInputs>
          {/* <SelectInputForm
            optionsArray={[]}
            label={"Motorista"}
            // {...register("licenseType")}
            // error={errors.licenseType}
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
          <RegInput
            type={"password"}
            placeholder={"Digite a senha do motorista"}
            id={"password"}
            label={"Senha"}
            {...register("password")}
            error={errors.password}
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
          /> */}
        </ContainerInputs>
        <div className="form__sendButton">
          <Button>ENVIAR</Button>
        </div>
      </form>
    </RegisterPageGeneric>
  );
};

export { TripRegister };
