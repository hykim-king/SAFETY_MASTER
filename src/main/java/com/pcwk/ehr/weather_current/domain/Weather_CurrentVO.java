package com.pcwk.ehr.weather_current.domain;

import java.util.Objects;

public class Weather_CurrentVO {

	private long weather_Id;
	private String gu_Cd;
	private double temp;
	private double min_Temp;
	private double max_Temp;
	private double feels_Like_Temp;
	private String weather_Desc;
	private String weather_Icon_Id;
	private int humidity;
	private double wind_Speed;
	private String ms_Dt;
	private int crt_By;
	private String crt_Dt;
	private int mod_By;
	private String mod_Dt;
	private String gu_Nm;

	public Weather_CurrentVO() {
		super();

	}

	public long getWeather_Id() {
		return weather_Id;
	}

	public void setWeather_Id(long weather_Id) {
		this.weather_Id = weather_Id;
	}

	public String getGu_Cd() {
		return gu_Cd;
	}

	public void setGu_Cd(String gu_Cd) {
		this.gu_Cd = gu_Cd;
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

	public String getMs_Dt() {
		return ms_Dt;
	}

	public void setMs_Dt(String ms_Dt) {
		this.ms_Dt = ms_Dt;
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
	

	public String getGu_Nm() {
		return gu_Nm;
	}

	public void setGu_Nm(String gu_Nm) {
		this.gu_Nm = gu_Nm;
	}

	@Override
	public int hashCode() {
		return Objects.hash(weather_Id);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Weather_CurrentVO other = (Weather_CurrentVO) obj;
		return weather_Id == other.weather_Id;
	}

	@Override
	public String toString() {
		return "Weather_CurrentVO [weather_Id=" + weather_Id + ", gu_Cd=" + gu_Cd + ", temp=" + temp + ", min_Temp="
				+ min_Temp + ", max_Temp=" + max_Temp + ", feels_Like_Temp=" + feels_Like_Temp + ", weather_Desc="
				+ weather_Desc + ", weather_Icon_Id=" + weather_Icon_Id + ", humidity=" + humidity + ", wind_Speed="
				+ wind_Speed + ", ms_Dt=" + ms_Dt + ", crt_By=" + crt_By + ", crt_Dt=" + crt_Dt + ", mod_By=" + mod_By
				+ ", mod_Dt=" + mod_Dt + ", gu_Nm=" + gu_Nm + "]";
	}



}
