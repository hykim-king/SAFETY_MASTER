package com.pcwk.ehr.weather_forecast.domain;

import java.util.Objects;

public class Weather_ForecastVO {

	private long fcst_Id;
	private String gu_Cd;
	private String fcst_Dt;
	private double temp;
	private double min_Temp;
	private double max_Temp;
	private double feels_Like_Temp;
	private String weather_Desc;
	private String weather_Icon_Id;
	private int humidity;
	private double wind_Speed;
	private double pop;
	private int crt_By;
	private String crt_Dt;
	private int mod_By;
	private String mod_Dt;
	private String week;

	public Weather_ForecastVO() {
		super();
	}

	public long getFcst_Id() {
		return fcst_Id;
	}

	public void setFcst_Id(long fcst_Id) {
		this.fcst_Id = fcst_Id;
	}

	public String getGu_Cd() {
		return gu_Cd;
	}

	public void setGu_Cd(String gu_Cd) {
		this.gu_Cd = gu_Cd;
	}

	public String getFcst_Dt() {
		return fcst_Dt;
	}

	public void setFcst_Dt(String fcst_Dt) {
		this.fcst_Dt = fcst_Dt;
	}

	public double getTemp() {
		return temp;
	}

	public void setTemp(double temp) {
		this.temp = temp;
	}

	public double getMin_Temp() {
		return min_Temp;
	}

	public void setMin_Temp(double min_Temp) {
		this.min_Temp = min_Temp;
	}

	public double getMax_Temp() {
		return max_Temp;
	}

	public void setMax_Temp(double max_Temp) {
		this.max_Temp = max_Temp;
	}

	public double getFeels_Like_Temp() {
		return feels_Like_Temp;
	}

	public void setFeels_Like_Temp(double feels_Like_Temp) {
		this.feels_Like_Temp = feels_Like_Temp;
	}

	public String getWeather_Desc() {
		return weather_Desc;
	}

	public void setWeather_Desc(String weather_Desc) {
		this.weather_Desc = weather_Desc;
	}

	public String getWeather_Icon_Id() {
		return weather_Icon_Id;
	}

	public void setWeather_Icon_Id(String weather_Icon_Id) {
		this.weather_Icon_Id = weather_Icon_Id;
	}

	public int getHumidity() {
		return humidity;
	}

	public void setHumidity(int humidity) {
		this.humidity = humidity;
	}

	public double getWind_Speed() {
		return wind_Speed;
	}

	public void setWind_Speed(double wind_Speed) {
		this.wind_Speed = wind_Speed;
	}

	public double getPop() {
		return pop;
	}

	public void setPop(double pop) {
		this.pop = pop;
	}

	public int getCrt_By() {
		return crt_By;
	}

	public void setCrt_By(int crt_By) {
		this.crt_By = crt_By;
	}

	public String getCrt_Dt() {
		return crt_Dt;
	}

	public void setCrt_Dt(String crt_Dt) {
		this.crt_Dt = crt_Dt;
	}

	public int getMod_By() {
		return mod_By;
	}

	public void setMod_By(int mod_By) {
		this.mod_By = mod_By;
	}

	public String getMod_Dt() {
		return mod_Dt;
	}

	public void setMod_Dt(String mod_Dt) {
		this.mod_Dt = mod_Dt;
	}

	public String getWeek() {
		return week;
	}

	public void setWeek(String week) {
		this.week = week;
	}

	@Override
	public int hashCode() {
		return Objects.hash(fcst_Id);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Weather_ForecastVO other = (Weather_ForecastVO) obj;
		return fcst_Id == other.fcst_Id;
	}

	@Override
	public String toString() {
		return "Weather_ForecastVO [fcst_Id=" + fcst_Id + ", gu_Cd=" + gu_Cd + ", fcst_Dt=" + fcst_Dt + ", temp=" + temp
				+ ", min_Temp=" + min_Temp + ", max_Temp=" + max_Temp + ", feels_Like_Temp=" + feels_Like_Temp
				+ ", weather_Desc=" + weather_Desc + ", weather_Icon_Id=" + weather_Icon_Id + ", humidity=" + humidity
				+ ", wind_Speed=" + wind_Speed + ", pop=" + pop + ", crt_By=" + crt_By + ", crt_Dt=" + crt_Dt
				+ ", mod_By=" + mod_By + ", mod_Dt=" + mod_Dt + ", week=" + week + "]";
	}

}
