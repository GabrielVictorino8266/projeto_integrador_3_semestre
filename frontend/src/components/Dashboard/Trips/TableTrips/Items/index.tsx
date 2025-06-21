import { StyledDriverList } from "./styles";
import type { Trip } from "@interfaces/trips.interface";
import { TripListItem } from "../Structure";

interface Props {
    data: Trip[];
}

export const TripList = ({ data }: Props) => {
    return (
        <StyledDriverList>
            {data.map((v) => {
                const date = new Date(v.startDateTime);
                const travelDate = date.toLocaleDateString("pt-BR"); 
                const departureTime = date.toLocaleTimeString("pt-BR", { hour: "2-digit", minute: "2-digit" }); 

                return (
                    <TripListItem
                        key={v.id}
                        id={v.id}
                        driverName={v.driverName ?? ""}
                        vehicle={v.driverId ?? ""}
                        destination={v.destination}
                        travelDate={travelDate}
                        departureTime={departureTime}
                        status={v.status}
                    />
                );
            })}
        </StyledDriverList>
    );
};
