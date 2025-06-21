export interface Trip {
    id: string;
    driverId: string;
    driverName?: string;
    startDateTime: string;
    endDateTime?: string;
    origin: string;
    destination: string;
    initialKm: number;
    finalKm?: number;
    completed: boolean;
    status: TripStatus
    createdAt: string;
    updatedAt: string;
}

export type TripStatus =  "active" | "cancelled" | "in_progress";

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
