import { tripCreateFormSchema } from "@schemas/tripCreateSchema";
import { z } from "zod";

export interface Trip {
  id: string;
  driverId: string;
  driverName?: string;
  startDateTime: string;
  vehicleLicensePlate: string;
  endDateTime?: string;
  origin: string;
  destination: string;
  initialKm: number;
  finalKm?: number;
  completed: boolean;
  status: TripStatus;
  createdAt: string;
  updatedAt: string;
}

export type TripStatus = "completed" | "in_progress" | "scheduled";

// Responses '-'

export interface TripsResponse {
  total: number;
  per_page: number;
  current_page: number;
  last_page: number;
  first_page_url: string;
  last_page_url: string;
  next_page_url?: string;
  prev_page_url?: string;
  path: string;
  from: number;
  to: number;
  items: Trip[];
}

export interface TripsIdResponse {
  id: string;
  driverName?: string | null;
  vehicleLicensePlate: string;
  startDateTime: string;
  origin: string;
  destination: string;
  initialKm: number;
  finalKm?: number | null;
  completed: boolean;
  status: TripStatus;
}

export type ICreateTripData = z.output<typeof tripCreateFormSchema>;

export interface ICreateTripResponse {
  id: string;
  driverId: string;
  startDateTime: string;
  endDateTime: string;
  origin: string;
  destination: string;
  initialKm: number;
  finalKm: number;
  completed: boolean;
  deleted: boolean;
  status: "pending" | "in_progress" | "completed" | "cancelled" | string;
  createdAt: string;
  updatedAt: string;
  deletedAt: string | null;
}

export interface ITripContextProps {
  createTrip: () => Promise<void>;
}
