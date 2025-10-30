export type RegisterRequest = {
  email: string;
  password: string;
  first_name?: string | null;
  last_name?: string | null;
};

export type RegisterResponse = {
  user_id: string;
  email: string;
  profile_completed: boolean;
};

export type LoginRequest = {
  email: string;
  password: string;
};

export type LoginResponse = {
  access_token: string;
  expires_in: number;
  refresh_token?: string | null;
};

export type PasswordForgotRequest = {
  email: string;
};

export type PasswordResetRequest = {
  token: string;
  password: string;
};

export type DashboardWidget = {
  id: string;
  type: string;
  data: Record<string, unknown>;
};

export type DashboardOverview = {
  user: {
    user_id: string;
    email: string;
    first_name?: string | null;
    last_name?: string | null;
    is_email_verified: boolean;
    last_login?: string | null;
  };
  stats: {
    logins_30d: number;
    tasks_completed: number;
  };
  widgets: DashboardWidget[];
};
