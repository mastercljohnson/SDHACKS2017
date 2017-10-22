package johnson.a2017sdhacks.tutorial.webservice;

import retrofit2.Call;
import retrofit2.http.GET;
import johnson.a2017sdhacks.tutorial.ServerTime;

/**
 * Created by mastercljohnson on 10/21/2017.
 */

public interface Api {
    @GET("/")
    public Call<ServerTime> getServerTime();
}
