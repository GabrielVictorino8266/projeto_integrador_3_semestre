import { Sidebar } from "@components/Sidebar";
import { ContainerInputs, Section } from "../Driver/styles";
import { RegisterPageGeneric } from "@components/RegisterForm";
import { RegInput } from "@components/InputForm";
import { SelectInputForm } from "@components/Select";
import { zodResolver } from "@hookform/resolvers/zod";
import { useForm, type SubmitHandler } from "react-hook-form";
import { tripFormSchema, type ITripFormRegister } from "@schemas/trip.schema";
import { useState } from "react";
import { statusTrip } from "@utils/Selects/statusTrip";
import { Button } from "@styles/Buttons";

const TripRegister = () => {
  const [inputTime, setInputTime] = useState("");
  const [inputDate, setInputDate] = useState("");

  const time24hMask = (value: string) => {
    let digits = value.replace(/\D/g, "").slice(0, 4);

    // Coloca ":" depois dos dois primeiros dígitos
    if (digits.length > 2) {
      digits = digits.replace(/^(\d{2})(\d{1,2})$/, "$1:$2");
    }

    return digits;
  };

  const dateMask = (value: string) => {
    return value
      .replace(/\D/g, "")
      .replace(/^(\d{2})(\d)/, "$1/$2")
      .replace(/^(\d{2})\/(\d{2})(\d)/, "$1/$2/$3")
      .slice(0, 10);
  };

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<ITripFormRegister>({
    resolver: zodResolver(tripFormSchema),
  });

  const submitTrip: SubmitHandler<ITripFormRegister> = async (
    registerForm: ITripFormRegister
  ) => {
    // handleCreateDriver(registerForm);
  };

  return (
    <Section>
      <Sidebar />
      <RegisterPageGeneric title="Cadastro de Viagens">
        <form>
          <ContainerInputs>
            <SelectInputForm
              optionsArray={[]}
              error={undefined}
              label="Motorista"
              id="driver"
            />
            <RegInput
              type={"text"}
              placeholder={"DD/MM/AAAA"}
              id={"data"}
              label={"Data da viagem"}
              value={inputDate}
              onChange={(event) => {
                setInputDate(dateMask(event.target.value));
              }}
            />
            <RegInput
              type={"text"}
              placeholder={"Insira o horário"}
              id={"time"}
              label={"Horário"}
              value={inputTime}
              onChange={(event) => {
                setInputTime(time24hMask(event.target.value));
              }}
            />
            <RegInput
              type={"text"}
              placeholder={"Digite a localização"}
              id={"local"}
              label={"Localização"}
            />
            <SelectInputForm
              optionsArray={[]}
              error={undefined}
              label="Veículo"
            />
            <SelectInputForm
              optionsArray={statusTrip}
              error={undefined}
              label="Status"
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

export { TripRegister };
