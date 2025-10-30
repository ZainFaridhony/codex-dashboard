import axios from "axios";

export const httpClient = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_BASE_URL ?? "http://localhost:8000",
  withCredentials: true
});
