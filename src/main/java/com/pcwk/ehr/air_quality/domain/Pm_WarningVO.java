package com.pcwk.ehr.air_quality.domain;

import java.util.Objects;

public class Pm_WarningVO {

	private String warn_Id;
	private String dist_Nm;
	private String move_Nm;
	private String issue_Item;
	private String issue_Gbn;
	private int issue_Conc;
	private String issue_Dt;
	private String clear_Dt;
	private int sn;
	private int crt_By;
	private String crt_Dt;
	private int mod_By;
	private String mod_Dt;

	public Pm_WarningVO() {
		super();
	}

	public String getWarn_Id() {
		return warn_Id;
	}

	public void setWarn_Id(String warn_Id) {
		this.warn_Id = warn_Id;
	}

	public String getDist_Nm() {
		return dist_Nm;
	}

	public void setDist_Nm(String dist_Nm) {
		this.dist_Nm = dist_Nm;
	}

	public String getMove_Nm() {
		return move_Nm;
	}

	public void setMove_Nm(String move_Nm) {
		this.move_Nm = move_Nm;
	}

	public String getIssue_Item() {
		return issue_Item;
	}

	public void setIssue_Item(String issue_Item) {
		this.issue_Item = issue_Item;
	}

	public String getIssue_Gbn() {
		return issue_Gbn;
	}

	public void setIssue_Gbn(String issue_Gbn) {
		this.issue_Gbn = issue_Gbn;
	}

	public int getIssue_Conc() {
		return issue_Conc;
	}

	public void setIssue_Conc(int issue_Conc) {
		this.issue_Conc = issue_Conc;
	}

	public String getIssue_Dt() {
		return issue_Dt;
	}

	public void setIssue_Dt(String issue_Dt) {
		this.issue_Dt = issue_Dt;
	}

	public String getClear_Dt() {
		return clear_Dt;
	}

	public void setClear_Dt(String clear_Dt) {
		this.clear_Dt = clear_Dt;
	}

	public int getSn() {
		return sn;
	}

	public void setSn(int sn) {
		this.sn = sn;
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

	@Override
	public int hashCode() {
		return Objects.hash(warn_Id);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Pm_WarningVO other = (Pm_WarningVO) obj;
		return Objects.equals(warn_Id, other.warn_Id);
	}

	@Override
	public String toString() {
		return "Pm_WarningVO [warn_Id=" + warn_Id + ", dist_Nm=" + dist_Nm + ", move_Nm=" + move_Nm + ", issue_Item="
				+ issue_Item + ", issue_Gbn=" + issue_Gbn + ", issue_Conc=" + issue_Conc + ", issue_Dt=" + issue_Dt
				+ ", clear_Dt=" + clear_Dt + ", sn=" + sn + ", crt_By=" + crt_By + ", crt_Dt=" + crt_Dt + ", mod_By="
				+ mod_By + ", mod_Dt=" + mod_Dt + "]";
	}

}
