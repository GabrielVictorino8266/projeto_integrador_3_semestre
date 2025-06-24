import { ContainerInputs } from "@components/Dashboard/Driver/CreateDriver/styles";
import { RegInput } from "@components/InputForm";
import { RegisterPageGeneric } from "@components/RegisterForm";
import { SelectInputForm } from "@components/Select";
import { zodResolver } from "@hookform/resolvers/zod";
import { useDriver } from "@hooks/useDriver";
import { useTrip } from "@hooks/useTrip";
import type {
  ICreateTripRequest,
  ITripFormData,
} from "@interfaces/trips.interface";
import { type IVehicle } from "@interfaces/vehicles.interface";
import { tripCreateFormSchema } from "@schemas/tripCreateSchema";
import { api } from "@services/api";
import { DarkBlueButton } from "@styles/Buttons";
import { dateMask, hourMask } from "@utils/reserve";
import { TripStatus } from "@utils/Selects/tripStatus";
import { useEffect, useState } from "react";
import { useForm, type SubmitHandler } from "react-hook-form";
import { GrMapLocation } from "react-icons/gr";

const TripRegister = () => {
  interface ISelectOptions {
    value: string;
    label: string;
  }

  const { getDriverList, driverList } = useDriver();
  const { createTrip } = useTrip();
  const [vehicleListData, setVehicleListData] = useState<Array<ISelectOptions>>(
    []
  );
  const [tripDateValue, setTripDateValue] = useState("");
  const [tripHourValue, setTripHourValue] = useState("");

  const [isLoading, setIsloading] = useState(true);

  const vehiclesList = async () => {
    try {
      const res = await api.get("/vehicles/");

      if (res.status === 200) {
        const vehicleListSelect: Array<ISelectOptions> = res.data.items.map(
          (vehicle: IVehicle) => ({
            value: vehicle.id,
            label: vehicle.licensePlate,
          })
        );
        setVehicleListData(vehicleListSelect);
      }
    } catch (error) {
      console.log(error);
    } finally {
      setIsloading(false);
    }
  };

  const driverListSelect: Array<ISelectOptions> = driverList.map((driver) => ({
    value: driver.id,
    label: driver.name,
  }));

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm({
    resolver: zodResolver(tripCreateFormSchema),
  });

  useEffect(() => {
    if (isLoading === true) {
      getDriverList();
      vehiclesList();
    }
    console.log("ok");
  }, [isLoading]);

  const submitTrip: SubmitHandler<ITripFormData> = (
    registerForm: ITripFormData
  ) => {
    const { tripDate, tripHour, ...rest } = registerForm;

    const newTripTreatedData: ICreateTripRequest = {
      ...rest,
      startDateTime: `${tripDate}T${tripHour}`,
    };
    console.log(newTripTreatedData);
    createTrip(newTripTreatedData);
  };

  return (
    <RegisterPageGeneric icon={<GrMapLocation />} title={"CADASTRO DE VIAGEM"}>
      <form onSubmit={handleSubmit(submitTrip)}>
        <ContainerInputs>
          <SelectInputForm
            optionsArray={driverListSelect}
            label={"Motorista"}
            {...register("driverId")}
            error={errors.driverId}
          />
          <SelectInputForm
            optionsArray={vehicleListData}
            id={"vehicle"}
            label={"Veículo"}
            {...register("vehicleId")}
            error={errors.vehicleId}
          />
          <RegInput
            type={"number"}
            placeholder={"ex: 10000"}
            id={"initialKM"}
            label={"Km do veículo"}
            {...register("initialKm", { valueAsNumber: true })}
            error={errors.initialKm}
          />
          <RegInput
            type={"text"}
            placeholder={"DD/MM/AAAA"}
            id={"tripDate"}
            label={"Data da viagem"}
            {...register("tripDate")}
            error={errors.tripDate}
            value={tripDateValue}
            onChange={(event) => {
              setTripDateValue(dateMask(event.target.value));
            }}
          />
          <RegInput
            type={"text"}
            placeholder={"HH:MM"}
            id={"tripHour"}
            label={"Horário"}
            {...register("tripHour")}
            error={errors.tripHour}
            value={tripHourValue}
            onChange={(event) => {
              setTripHourValue(hourMask(event.target.value));
            }}
          />
          <RegInput
            type={"text"}
            placeholder={"Ex: Leme"}
            id={"origin"}
            label={"Origem"}
            {...register("origin")}
            error={errors.origin}
          />
          <RegInput
            type={"text"}
            placeholder={"Ex: São Paulo"}
            id={"destination"}
            label={"Destino"}
            {...register("destination")}
            error={errors.destination}
          />
          <SelectInputForm
            optionsArray={TripStatus}
            id={"tripStatus"}
            label={"Status"}
            {...register("status")}
            error={errors.status}
          />
        </ContainerInputs>
        <div className="form__sendButton">
          <DarkBlueButton>ENVIAR</DarkBlueButton>
        </div>
      </form>
    </RegisterPageGeneric>
  );
};

export { TripRegister };
